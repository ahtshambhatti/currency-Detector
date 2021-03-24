from utils import *
from matplotlib import pyplot as plt
import os
from playsound import playsound

import subprocess
from gtts import gTTS

max_val = 8
max_pt = -1
max_kp = 0

orb = cv2.ORB_create()
# orb is an alternative to SIFT
# --------------------------------------------------------
cap = cv2.VideoCapture(0)

# # loop runs if capturing has been initialized 
while(1): 

    # reads frame from a camera 
    ret, frame = cap.read() 

    # Display the frame
    cv2.imshow('Camera',frame) 

    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # saving the frame image
        cv2.imwrite('files/frame.png', frame)
        break

# release the camera from video capture
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
# ------------------------------------------------------------
    # 'Training/Ten riyals/Ten riyal(1).jpg'
test_img = read_img('files/frame.png')
# test_img = read_img('files/Ten riyal(1).jpg')
# test_img = read_img('files/20 riyals.jp eg')
#test_img = read_img('files/test_100_3.jpg')
#test_img = read_img('files/test_20_4.jpg')

# resizing must be dynamic
original = resize_img(test_img, 0.4)
display('original', original)

# keypoints and descriptors
# (kp1, des1) = orb.detectAndCompute(test_img, None)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set = [
    'Training/Fifty riyals/Fifty riyal(1).jpg',
    'Training/Fifty riyals/Fifty riyal(2).jpg',
    'Training/Fifty riyals/Fifty riyal(3).jpg',
    'Training/Fifty riyals/Fifty riyal(4).jpg',
    'Training/Fifty riyals/Fifty riyal(5).jpg',
    'Training/Fifty riyals/Fifty riyal(6).jpg',
    'Training/Fifty riyals/Fifty riyal(7).jpg',
    'Training/Fifty riyals/Fifty riyal(8).jpg',
    'Training/Fifty riyals/Fifty riyal(9).jpg',
    'Training/Ten riyals/Ten riyal(1).jpg',
    'Training/Ten riyals/Ten riyal(2).jpg',
    'Training/Ten riyals/Ten riyal(3).jpg',
    'Training/Ten riyals/Ten riyal(4).jpg',
    'Training/Ten riyals/Ten riyal(5).jpg',
    'Training/Ten riyals/Ten riyal(6).jpg',
    'Training/Ten riyals/Ten riyal(7).jpg',
    'Training/Ten riyals/Ten riyal(8).jpg',
    'Training/Ten riyals/Ten riyal(9).jpg',
    'Training/Ten riyals/Ten riyal(10).jpg', 
    'Training/One hundred riyals/One hundred riyal(1).jpg',
    'Training/One hundred riyals/One hundred riyal(2).jpg',
    'Training/One hundred riyals/One hundred riyal(3).jpg',
    'Training/One hundred riyals/One hundred riyal(4).jpg',
    'Training/One hundred riyals/One hundred riyal(5).jpg',
    'Training/One hundred riyals/One hundred riyal(6).jpg',
    'Training/One hundred riyals/One hundred riyal(7).jpg',
    'Training/One hundred riyals/One hundred riyal(8).jpg',
    'Training/One hundred riyals/One hundred riyal(9).jpg',
    'Training/One hundred riyals/One hundred riyal(10).jpg',
    'Training/Five hundred riyals/Five hundred riyal(1).jpg',
    'Training/Five hundred riyals/Five hundred riyal(2).jpg',
    'Training/Five hundred riyals/Five hundred riyal(3).jpg',
    'Training/Five hundred riyals/Five hundred riyal(4).jpg',
    'Training/Five hundred riyals/Five hundred riyal(5).jpg',
    'Training/Five hundred riyals/Five hundred riyal(6).jpg',
    'Training/Five hundred riyals/Five hundred riyal(7).jpg',
    'Training/Five hundred riyals/Five hundred riyal(8).jpg',
    'Training/Five hundred riyals/Five hundred riyal(9).jpg',
    'Training/Five hundred riyals/Five hundred riyal(10).jpg',
    'Training/Five riyals/Five riyal(1).jpg',
    'Training/Five riyals/Five riyal(2).jpg',
    'Training/Five riyals/Five riyal(3).jpg',
    'Training/Five riyals/Five riyal(4).jpg',
    'Training/Five riyals/Five riyal(5).jpg',
    'Training/Five riyals/Five riyal(6).jpg',
    'Training/Five riyals/Five riyal(7).jpg',
    'Training/Five riyals/Five riyal(8).jpg',
    'Training/Five riyals/Five riyal(9).jpg',
    'Training/Five riyals/Five riyal(10).jpg',
    'Training/One riyal/One riyal(1).jpg',
    'Training/One riyal/One riyal(2).jpg',
    'Training/One riyal/One riyal(3).jpg',
    'Training/One riyal/One riyal(4).jpg',
    'Training/One riyal/One riyal(5).jpg',
    'Training/One riyal/One riyal(6).jpg',
    'Training/One riyal/One riyal(7).jpg',
    'Training/One riyal/One riyal(8).jpg',
    'Training/One riyal/One riyal(9).jpg',
    'Training/One riyal/One riyal(10).jpg',
]
for i in range(0, len(training_set)):
	# train image
	train_img = cv2.imread(training_set[i])

	(kp2, des2) = orb.detectAndCompute(train_img, None)

	# brute force matcher
	bf = cv2.BFMatcher()
	all_matches = bf.knnMatch(des1, des2, k=2)

	good = []
	# give an arbitrary number -> 0.789
	# if good -> append to list of good matches
	for (m, n) in all_matches:
		if m.distance < 0.789 * n.distance:
			good.append([m])

	if len(good) > max_val:
		max_val = len(good)
		max_pt = i
		max_kp = kp2

	print(i, ' ', training_set[i], ' ', len(good))

if max_val != 8:
	print(training_set[max_pt])
	print('good matches ', max_val)

	train_img = cv2.imread(training_set[max_pt])
	img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
	
	note = str(training_set[max_pt]).split('/')

	print('\nDetected denomination: Rs. ', note[1])

	audio_file = 'audio/{}.mp3'.format(note)
	#audio_file = "value.mp3"
	#tts = gTTS(text=speech_out, lang="en")
	#tts.save(audio_file)
	#return_code = subprocess.call(["afplay", audio_file])
	#playsound(audio_file)
	(plt.imshow(img3), plt.show())

else:
	print('No Matches')
