# Q-Rand-Num
This is a Quantum Bitstring Generator

# Getting Started
- **Before running the below always ensure your in the correct directory.**
- **While running the Desktop app you please press enter once you've entered a number in the text box.**
- To get started make sure you have python 3.6 or later and pip installed
- Run the command on bash (preferably) on Mac or Linux and on Command Prompt(preferably) on Windows
## On Windows:
- **For some reason the text in the edges won't appear. And for a moment the Main Window might show Not Responding but then it should be fine in a while**

## For MacOS and Linux:
1) Run:
**If you have get any errors in running this then run `2.`**
```
./setup.sh
```
2) Run:
```
./fixed.sh
```
3) Run:
```
./requirements.sh
```
4) Now finally to run the app:
```
python main.py
```
**If this doesn't work then run**:
```
python3 main.py
```
## For Windows:
1) In your Command Prompt:
```
.\setup.bat
```
2)
```
.\requirements.bat
```
3) Now finally to run the app:
```
python main.py
```
# Note:
- As this is using Qiskit and IBM Quantum, the actual quantum computer as of now will be noisy and there could be a long queue on public devices. So it is using QASM Simulator as of now.

## Acknowledgments
- This project is inspired from [Samsung’s new phone has a 2.5 mm quantum random number generator for improved security](https://thenextweb.com/news/samsungs-new-phone-has-a-2-5-mm-quantum-random-number-generator-for-improved-security)
- Photo by [Fractal Hassan](https://unsplash.com/photos/XoNj0ulsn1Y) on [Unsplash](https://unsplash.com/)
- I used some code for [importing a python script from StackOverflow](https://stackoverflow.com/questions/2349991/how-to-import-other-python-files)
