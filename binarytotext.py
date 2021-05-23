asciii = {
      "32": " ",
      "33": "!",
      "34": "\"",
      "35": "#",
      "36": "$",
      "37": "%",
      "38": "&",
      "39": "\'",
      "40": "(",
      "41": ")",
      "42": "*",
      "43": "+",
      "44": ",",
      "45": "-",
      "46": ".",
      "47": "/",
      "48": "0",
      "49": "1",
      "50": "2",
      "51": "3",
      "52": "4",
      "53": "5",
      "54": "6",
      "55": "7",
      "56": "8",
      "57": "9",
      "58": ":",
      "59": ";",
      "60": "<",
      "61": "=",
      "62": ">",
      "63": "?",
      "64": "@",
      "65": "A",
      "66": "B",
      "67": "C",
      "68": "D",
      "69": "E",
      "70": "F",
      "71": "G",
      "72": "H",
      "73": "I",
      "74": "J",
      "75": "K",
      "76": "L",
      "77": "M",
      "78": "N",
      "79": "O",
      "80": "P",
      "81": "Q",
      "82": "R",
      "83": "S",
      "84": "T",
      "85": "U",
      "86": "V",
      "87": "W",
      "88": "X",
      "89": "Y",
      "90": "Z",
      "91": "[",
      "92": "\\",
      "93": "]",
      "94": "^",
      "95": "_",
      "96": "`",
      "97": "a",
      "98": "b",
      "99": "c",
      "100": "d",
      "101": "e",
      "102": "f",
      "103": "g",
      "104": "h",
      "105": "i",
      "106": "j",
      "107": "k",
      "108": "l",
      "109": "m",
      "110": "n",
      "111": "o",
      "112": "p",
      "113": "q",
      "114": "r",
      "115": "s",
      "116": "t",
      "117": "u",
      "118": "v",
      "119": "w",
      "120": "x",
      "121": "y",
      "122": "z",
      "123": "{",
      "124": "|",
      "125": "}",
      "126": "~",
   }

def format_input():
   print("User: ", end = "")
   inputInfo = input("")
   print("\"" + inputInfo + "\"")
   return inputInfo

def check_correct_input(input):
   pieces = input.split(" ")
   format = True
   errorMessage = ""
   for binary in pieces:
      if len(binary) != 8:
         format = False
         errorMessage = "- Each piece of binary must be exactly 8 characters long."
      for char in binary:
         if char != "0" and char != "1":
            format = False
            if len(errorMessage) > 0 and "only use" not in errorMessage:
               errorMessage += "\n"
            if "only use" not in errorMessage:
               errorMessage += "- You must only use 1s and 0s in the binary code." 
   return format, errorMessage

def binary_to_num(binary):
   numbers = binary.split(' ')
   newNums = []
   for number in numbers:
      total = 0
      index = len(number) - 1
      for char in number:
         if char == "1":
            total += 2**index
         index -= 1
      newNums.append(str(total))
   return newNums

def num_to_letter(nums):
   string = ""
   for num in nums:
      if num not in asciii:
         return False, "I'm sorry, there has been an error. The binary code you've entered doesn't match any characters."
      string = string + asciii[num]
   return True, string

def binary_to_string(binary):
   numberList = binary_to_num(binary)
   works, fullstring = num_to_letter(numberList)
   return works, fullstring

print("Welcome to the binary to text converter! In this application, you can enter your binary code and it will be converted to text. \nFor more information about binary to text, go to bit.ly/binary-text. \n *Note: Your input should be chunks of binary, each 8 characters long, separated by spaces (a space denotes a new character), and written only using 1s and 0s.")

running = True
while running:
   print("\nPlease enter the binary code you would like to convert to text.")
   string_to_convert = format_input()
   correct_input, errMessage = check_correct_input(string_to_convert)
   if not correct_input:
      print("\nI'm sorry, there has been an error(s):")
      print(errMessage)
   else:
      works, converted_string = binary_to_string(string_to_convert)
      if works:
         print("\n The text version of that string is: \n "+converted_string)
      else:
         print(converted_string)
   
   print("\n Would you like to use the binary to text converter again? ")
   keepGoing = format_input()
   if "ye" not in keepGoing:
      running = False
   else:
      print("Ok, bye!")