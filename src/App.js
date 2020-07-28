import React from 'react';
import './App.css';
import {Container, Row, Navbar} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Mic from "./mic";
// import "bootstrap/dist/js/bootstrap";

function App() {
  return (
      <div>
          <div className="background"/>
          <Navbar style={{backgroundColor:"rgba(0,0,179,0.24)"}}>
              <Navbar.Text className="header-texts">SIGNALS AND SYSTEMS PROJECT</Navbar.Text>
              <Navbar.Toggle />
              <Navbar.Collapse className="justify-content-end">
                  <Navbar.Text className="header-texts">
                     YES NO RECOGNIZER
                  </Navbar.Text>
              </Navbar.Collapse>
          </Navbar>
          <Container className="mt-5">
              <Row className="justify-content-center">
                  <Mic/>
              </Row>
          </Container>
          <svg style={{position:"fixed",bottom:0,left:0}} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#ffffb1" fill-opacity="1" d="M0,288L48,245.3C96,203,192,117,288,117.3C384,117,480,203,576,250.7C672,299,768,309,864,298.7C960,288,1056,256,1152,245.3C1248,235,1344,245,1392,250.7L1440,256L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>
      </div>
  );
}

export default App;
