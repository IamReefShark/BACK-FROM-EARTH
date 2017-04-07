#include "ofApp.h"

void ofApp::setup(){
    
    ofBackground(0);
    

}

void ofApp::update(){
    
    for(int i = 0; i < 100000; i++){
        
        float x = random(width/2);
        float y = random(height);
        point(x,y);
    
    }

}


void ofApp::draw(){
    
    ofSetColor(255);
    ofDrawCircle(500, 500, 80);

}








