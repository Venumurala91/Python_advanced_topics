

# # '''
# # with open('C:\\Users\\Venugopal\\Downloads\\new 3.txt', 'r') as file:
# #     content = file.read()
# #     print(content)




# # with open(r'C:\Users\Venugopal\Downloads\new_file.txt', 'a') as file:
# #     # Content to write to the file
# #     content = '''Hello, this is a test file.
# # This is the second line.
# # Python makes file handling easy!
# # We can add multiple lines of text.
# # '''
# #     file.write(content)
# #     file.close()
   
# # print("Content written to the file successfully.")

# # '''



# # Read content from the existing file
# with open('C:\\Users\\Venugopal\\Downloads\\new 3.txt', 'r') as file:
#     content = file.read()
#     print("Original content of the file:")
#     print(content)

# # Now, append content to the same file ('new 3.txt')
# with open('C:\\Users\\Venugopal\\Downloads\\new 3.txt', 'a') as file:
#     additional_content = '''Hello, this is a test file.
# This is the second line.
# Python makes file handling easy!
# We can add multiple lines of text.
# '''
#     file.write(additional_content)

# print("Content appended to the same file successfully.")

# # Reopen the file to read the updated content after appending
# with open('C:\\Users\\Venugopal\\Downloads\\new 3.txt', 'r') as file:
#     updated_content = file.read()
    
#     print("\nUpdated content of the file after appending:")
#     print(updated_content)



# with open('C:\\Users\\Venugopal\\Downloads\\new 3.txt','a') as file:
#     new_content = ''' THIS IS SECOND CONTENT TO ADDING TO YOUR OLD FILE '''

#     adding_second_content = file.write(new_content)

#     print("\n Hello! User this is appended third content")



# with open("C:\\Users\\Venugopal\\Downloads\\test.txt",'a') as file:
#     content = '''THIS IS NEW TEST CONTENT 
#     THIS IS NEW TEST CONTENT 
#     THIS IS NEW TEST CONTENT 
#     THIS IS NEW TEST CONTENT THIS IS NEW TEST CONTENT THIS IS NEW TEST CONTENT THIS IS NEW TEST CONTENT 
#     '''

#     file.write(content)

#     file.truncate(10)




# with open("C:\\Users\\Venugopal\\Downloads\\test.txt", 'r+') as file :
#     content= ''' \nHello this is read and write methods with'''
#     # writee= file.write(content) 
#     readd=file.read()
#     print(readd)
#     # print(writee)
    
    


with open("C:\Users\Venugopal\Downloads\test_binary.txt", 'rb+') as file:
    Binary_content = "hello 1 5 4 "

    writee = file.write()


