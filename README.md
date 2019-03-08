## ML-HACKSRPINT
ML-HACKSPRINT DSC BVP tensorflow watch party hackathon code

# IDEA 
The theme chosen for this project was entertainment. 

Tensorflow's deep dreamer is famous for generating trippy and artistic images from as little definite information as random noise and works like a charm on actual images : 

![the-starry-night-800x450](https://user-images.githubusercontent.com/24889667/54002515-d9f16b00-4174-11e9-951f-5cad45c6fd85.jpg)

                                                     original image 

![dream_image_out](https://user-images.githubusercontent.com/24889667/54002526-e4ac0000-4174-11e9-8dac-bdd391860df3.jpg)

                                                     transformed image 

An audio file can be seen as an array. 1 second of an audio file generally has 44100 values which is = 210 x 210 ( I am no expert in this field but I'd say they did this to make matrix operations easier for normal sound modifications )

I used the deep-dreamer as an adhoc "transformer". 

Original audio, reshaped to 210x210x3 (notice there's no RGB component)

![original](https://user-images.githubusercontent.com/24889667/54002272-fd67e600-4173-11e9-9990-bac587a9e047.jpg)

transformed audio : 

![transformed](https://user-images.githubusercontent.com/24889667/54002274-02c53080-4174-11e9-95cb-f5cc79db16a3.jpg)

