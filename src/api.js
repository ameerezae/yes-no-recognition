import axios from "axios";

class VoiceRecordApi {
    static async sendWavVoice(wavFile){
        try{
            let formData = new FormData();
            formData.append("audio-file", wavFile);
            const response = await axios.post(
                "http://51.195.53.45:5000/yes_no_detection",
                formData,
                {
                    headers : {
                        'Content-Type' : 'multipart/form-data'
                    },
                }
            )
            if(response) return response;

        }catch (e) {
            if(e.response) return e.response;
        }
    }
}

export default VoiceRecordApi;