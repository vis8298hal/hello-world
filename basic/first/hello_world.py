def hello_world():
  name = input("Enter your Name Please");
  result_str = f"""<HTML>
                <head>
                  <title>Welcome {name}</title>
                  </head>
                  <body>
                    <h1>Hello World ! </h1>
                    <h1>I am {name} </h1>
                    <h2>I am new to Programming</h2>
                  </body>
                </HTML> """
  file1 = open("hello_world.html", "w")
  file1.writelines(rseult_str)
  file1.close()
