# ML-HACKSRPINT
ML-HACKSPRINT DSC BVP tensorflow watch party hackathon code

## IDEA 
The theme chosen for this project was entertainment. 

Tensorflow's deep dreamer is famous for generating trippy and artistic images from as little definite information as random noise and works like a charm on actual images : 

![the-starry-night-800x450](https://user-images.githubusercontent.com/24889667/54002515-d9f16b00-4174-11e9-951f-5cad45c6fd85.jpg)

                                                     original image 

![dream_image_out](https://user-images.githubusercontent.com/24889667/54002526-e4ac0000-4174-11e9-8dac-bdd391860df3.jpg)

                                                     transformed image 

An audio file can be seen as an array. 1 second of an audio file generally has 44100 values which is = 210 x 210 ( I am no expert in this field but I'd say they did this to make matrix operations easier for normal sound modifications )

I used the deep-dreamer as an adhoc "transformer". 

Original audio, reshaped to 210x210x3 (notice there's very little RGB component)

![original](https://user-images.githubusercontent.com/24889667/54002272-fd67e600-4173-11e9-9990-bac587a9e047.jpg)

transformed audio : 

![transformed](https://user-images.githubusercontent.com/24889667/54002274-02c53080-4174-11e9-95cb-f5cc79db16a3.jpg)

now the results aren't out of this world. Initially, it appears to simply be adding white noise (if you run it over the entire audio file). However, that may not necessarily be the case because in order to construct one RGB image, we look 3 seconds into the future( 3 seconds at a time are transformed ). When it performs a transformation, the transformation at the current time instant is in a way linked to the original value 1 second and 2 second into the future. This effect is more prominent (and appreciable) around beat drops. 

Do note that the method does not alter the underlying notes of the audio file.

For best experience please use bass boosted earphones

## SCOPE OF USE : 
The applications for this are not limited to entertainment, however, this was created for the purposes of boosting the entertainment industry. This isn't a perfect end product yet (since I only have no past experience in sound engineering). However, in the future, you could remix your music using AI to introduce new sounds into an already poppy song.  
