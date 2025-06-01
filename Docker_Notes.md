![image](https://github.com/user-attachments/assets/1341b7f6-02a9-452e-9f36-7f8f18d20ec5)

# **We will divide the terms into components for better understanding:**

![image](https://github.com/user-attachments/assets/9099fb7d-e49e-4612-a99c-50b86e7483ec)

![image](https://github.com/user-attachments/assets/9fb0cc5e-ad38-4f66-9085-95d4f44e31b7)

![image](https://github.com/user-attachments/assets/7918d291-69de-472f-965e-1f6441912d96)
![image](https://github.com/user-attachments/assets/f63ee137-f3b7-4be0-a2ea-5402cdd0a14b)

* ``Books on shelves = storage. They just sit there.``

* ``Librarian handing a book to you at checkout or mailing a book to another branch = distribution. The book is traveling from one place to another.``

![image](https://github.com/user-attachments/assets/89867486-e366-49ce-a70b-77711c097e92)

# **The ``storage`` step in docker image lifecycle acts as a registry**

![image](https://github.com/user-attachments/assets/72513afb-2f73-48b5-b1be-1168af0b50cc)
![image](https://github.com/user-attachments/assets/77f93d71-8b0d-43a4-8346-41ab5f8a275c)

![image](https://github.com/user-attachments/assets/941873c5-655c-46d3-9e27-4d6de553264e)


# **Pulling and Running the Images:**

* For example, to run hello-world image, we can search the docker-hub to get the command:
``docker pull hello-world``

to execute it, we will use the terminal of Docker Desktop or we can even use cmd:
``docker run hello-world``


# **Now we will learn how to create an image and store it in the registry**

* Lets say we have a .py file already with us having the required code.

* We have a requirements.txt file

* Now we will create a Dockerfile having these things listed in it (BWCRPC) --> ``Base image, working dir, copy, run, port, command``

