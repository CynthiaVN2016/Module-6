# Module 6 Task 1 - Distributed Networks 

## Table of Contents  
* [Idea](#idea)  
* [Implementation](#implementation)
* [Final Results](#final)
* [Difficulties](#difficulties)
  
<a name="idea"/>

## Idea
Since all our sensors were in the kitchen, my goal was to make it very cohesive. I struggled thinking of an idea, but thought now was a good time to challenge myself and try something new. With that in mind, I wanted to include sound into my presentation. I decided to make each sensor correspond to a different sound that would play off of my Raspberry Pi. I wanted to create a home-like atmosphere, and that influenced many of my audio choices.

<a name="implementation"/>

## Implementation

* ESP32
* Raspberry Pi 3 B+
* Speakers w/ audio jack
* Various sound files

These materials above are more relevant to task 2. For task 1, every member in the group was in charge of making a sensor and having that information transmitted on the network. My Raspberry Pi would pick up on the data from the sensor and output corresponding audio files detailed below alongside the sensor information.

* Door sensor (ultrasonic sensor) - this sensor was mounted above the door to detect movement in and out of the door. Every detection resulted in an audio file of me saying "Welcome Home."
* Freezer sensor (capacitive touch sensor) - the sensor was attached to the handle of the freezer. While it is being touched, an audio file of food cooking on the stove is played.
* Cabinet sensor (button) - the sensor was located inside the cabinet to detect whether it is open or not. When the cabinet is open, the sound of placing bowls and plates on the table to output.
* Microwave sensor (piezoelectric sensor) - the sensor was located on the main button of the microwave. Touching that lead to an ASMR audio clip of someone eating crunchy food.

The door, microwave, and freezer sensor were not near outlets, so those were powered by LiPo batteries. We were able to connect the cabinet sensor/ESP to the outlet due to its proximity, but also because of its need for additional power (one group members added motors to this ESP).

We used painlessMesh to create a network amongst all the sensors/ESP32, but since I was working with sound, I wanted to figure out how to get my Raspberry Pi to join the Network and take in all the sending messages to process it. My peer recommended painlessMeshBoost to install and run on my Pi, and it was successful.

I was able to join the network with my pi and read the incoming messages; however, the next big hurdle was to figure out how those messages could be streamed into the various audio applications on the Pi. I considered SuperCollider and Sonic Pi, but that did not seem feasible with my lack of knowledge on these software. Luckily, I found out that Pi supported OMXPlayer, which is an accelerated command line media player. This allowed to my use extraneous software.

I first made individual shell scripts that would play each audio file. I then created a python script that would take in the messages coming in through painlessMeshBoost as stdin. Based on the information it received, it would spawn a new process that runs the appropriate shell script, essentially playing the audio file. Once it receives any information indicating that the users stopped interacting with the objects in the kitchen (e.g. Touching the freezer and releasing it), it runs another script that kills all processes related to the OMXPlayer.

I had to configure the Pi to play audio from the audio jack. Once that was done, I attached the external speakers, and everything was ready to go!

<a name="final"/>

## Final Result

Everything worked out okay. There were times the correct audio was not output, but those issues stemmed from the messages being sent from the sensor.

My group mates and I did not coordinate as well when deciding what to pursue as a final project for this task, so 3/4 of us relied on sound. This made the following demo video quite hectic below, and I am not sure how well everything could be heard. I should have made more effort to properly record a demo of my kitchen sounds, but I will keep that in mind for next time.

<a name="difficulties"/>

## Difficulties 

* Ran into some problems with running processes in the shell and killing them
* Working with the changing IP address of the Pi once it was on the ESP's network
