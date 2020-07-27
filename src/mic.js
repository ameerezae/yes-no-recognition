import React, {Component} from "react";
import "./index.css";
import AudioAnalyser from "react-audio-analyser";
import {Row} from "react-bootstrap";
import MicButton from "./mic-button";
import Swal from "sweetalert2";
import VoiceRecordApi from "./api";

class Mic extends Component {
    constructor(props) {
        super(props)
        this.state = {
            audioProps: {
                status: "",
                audioType: "audio/wav",
                audioOptions: {sampleRate: 44100},
                timeslice: 1000,
                backgroundColor: 'transparent',
                strokeColor: 'white',
                width: "600"
            },
            spinner : false,
        }
    }

    controlAudio(status) {
        this.setState(prevState => {
            const newState = {...prevState};
            newState.audioProps.status = status;
            return newState;
        })
    }

    convertBlobToFile(blob) {
        return new File([blob], "audio.wav", {type: "audio/wav"});
    }

    startRecording() {
        setTimeout(() => {
            this.setState(prevState => {
                const newState = {...prevState};
                newState.audioProps.status = "inactive";
                return newState;
            })
        }, 2000)
    }

    async finishRecording(blob) {
        const audioFile = this.convertBlobToFile(blob);
        this.setState({spinner:true});
        const response =  await VoiceRecordApi.sendWavVoice(audioFile);
        if(response.data) {
            Swal.fire(
                response.data.result,
                response.data["feature_value"].toString(),
            )
            this.setState({spinner:false});
        }else{
            console.log("not fetched!")
        }
    }


    render() {
        return (
            <div>
                <AudioAnalyser
                    {...this.state.audioProps}
                    startCallback={(e) => (this.startRecording(e))}
                    stopCallback={(e) => (this.finishRecording(e))}
                >
                    <Row className="justify-content-center">
                        {this.state.audioProps.status !== "recording" &&
                        <div className="buttons" onClick={() => {this.controlAudio("recording")}}>
                            <MicButton/>
                        </div>}
                    </Row>
                </AudioAnalyser>
            </div>
        );
    }
}

export default Mic