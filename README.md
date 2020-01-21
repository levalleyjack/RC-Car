# RC-Car
## Dependencies
- [x] PyNMEA2
- [x] Flask
- [x] GPIO
- [x] Unity
- [ ] GeoPy
## Summary
Our team developed an RC car which uses the Python language executed on a Raspberry Pi to drive a car. The car is controlled through POST requests sent from Unity. Our Raspberry Pi uses a separate motor controller connected to DC motors in order to drive the vehicle. These connections are all possible due to a 40 pin header on the Raspberry Pi and an internet connection. This header allows power and information to be transfered to the motor controller. The internet connection allows the connection with Unity for the user to drive the car. Running the code and updating the code all are all done over this internet connection. For our libraries used, the GPIO library tells the code to send and receive information over the pins on the header. The Flask library controls the back-end operations for the POST requests from Unity.
