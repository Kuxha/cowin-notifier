# cowin-notifier
For getting alerts | notifications for availability of vaccination slots.

This script is totally hardcoded for now
All I have done is add a while loop that calls the function every two mins, if the number of sessions is greater than 0, it plays the sound.

How to get the district or State number 

Method 1 : run the getState() , and then using that state number run getDistrict()
Method 2 : go to cowin website. do inspect element. send the request, you will see the url on the network tab

P.S - Do not forget to put a mp3 file and put its url in the playsound() function
