# Lab 3 Break The Caesar Cipher
Caesar used a cypher when he wanted to transmit coded messages on his military campaigns. In those days, as nowadays,
security was a problem, so he used that cipher.

Caesar cipher is a simple shift technique to replace each letter of the alphabet with another letter further down the alphabet.
In the first century B.C. it was enough to ensure that his messages couldn't be read unless the receiver knew the secret.

Due to the simple nature of the Caesar cipher, it could easily be brute forced by trying all possible 25 keys and then looking by
eye to see if the plaintext was revealed. Bu more interesting and wise method is frequency analysis, which can be used to decipher the Caesar cipher.
There are 26 letters in the English alphabet, but they don’t each appear an equal amount of the time in English text.
Some letters are used more often than others. The letters as E, T, A and O occur very frequently in English words.But the letters J, X, Q, and Z are rarely found in English text. 

Using the following code we can use frequency analysis to find the solution to a ciphertext. In each rotation will be calculated some error 
in dependence of frequency of each letter. If is used a sufficient long section of encrypted text, error could be minimized and find out the 
rotation which was used to encrypt.

Result is:

![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%233/results.PNG "Deciphered Caesar cipher")
