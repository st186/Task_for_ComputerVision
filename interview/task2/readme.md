** My Approach **

In this task first I looked at the annotation.xml file and found out that it is not feasible to perform a object detection model because of the absense of coodinates for face mask and safety helmets. We just had head coordinates and just class labels for mask and helmet. So, I thought it would be better if we go with an approach where we can just crop out the head using the coordinates and then convert this into a multi label classification problem.

There were two classes - helmet and mask

Within mask there are 4 classes - yes, no, invisible, wrong but we went ahead with two classes only yes or no because we didnt have much dataset to generalise it

Within helmet we had 2 classes - yes or no
