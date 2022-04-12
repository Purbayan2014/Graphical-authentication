# Graphical-authentication

This is used to increase the protection/security of a website. The system is divided into further 3 layers of protection. Each layer is totally different and diverse than the others. This not only increases protection, but also makes sure that no non-human can log in to your account using different activities such as Brute Force Algorithm and so on.

1.Segmented Images Authentication

For this layer, the user will be showed 4 different images. These images will be a division of a whole image. User will have to select the correct order of the images.




2.Password Image Authentication

For this layer,Whenever a user registers, he/she is asked to select an image category from the 3 given categories:

Cat
Mouse
Flower
Whatever the user selects, is associated with his/her password and every time the user logs in, he/she will be asked to select the same image from the randomly displayed images.

Now here’s the twist I have stored multiple images for each category. So, if a user selects cat, he/she will not be displayed the same cat every single time. The images per category are different as can be seen below.

a) Cat:



b) Mouse:



c) Flower:



According to my  implementation, I have stored 3 categories i.e., cat, mouse, flower in our database. Whatever the user has selected while registering has been stored into the database along with his password. Each category has 3 different versions named 0, 1, 2. At the start of the program, a random number is generated between 0 and 2. Whatever the number is, is the picture of each category that is to be displayed. This is to just add a bit more complexity to the code.



3.Garbled Images Authentication

The last and the most difficult layer is the garbled text authentication. In this layer, the user will be displayed a Garbled text whose readability will be really low and user will be asked to read and then type in the text. 


# Strengths
Graphical passwords are a more secure alternative to standard text-based passwords, especially as they don’t significantly lower usability. Using graphical password authentication, we can avoid the problem of keystroke logging, and be protected against dictionary attacks and social engineering. This technique for user authentication also requires human interaction on part of the user, which doubles as verifying the user was a human without having to make use of CAPTCHA 

