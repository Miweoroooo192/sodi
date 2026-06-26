import sys
import os
import time

if len(sys.argv) == 2:
    print("this is sodi")
    if sys.argv[1] == "make":
        
        try:
            os.makedirs("sodi")
            file = open("sodi/sodi_config.txt", "w")
            file.write("Build=1\ntargetFile=sobitext.txt")
            file.close()
            print("Project made, try running the program with the run argument to run!")
        except FileExistsError:
            print("Error: Project already exists, try running with the run argument.")
        except Exception as e:
            print("Error: " + str(e))
    elif sys.argv[1] == "run":
        try:
            print("Running!")
            build = None
            targetfile = None
            with open("sodi/sodi_config.txt", "r") as file:
                for options in file:
                    if "Build" in options:
                        buildinconfig = options.strip()
                        build = int(buildinconfig.replace("Build=", ""))
                        buildnum = int(build)
                    if "targetFile" in options:
                        gettargetfilefromconfig = options.strip()
                        targetfile = gettargetfilefromconfig.replace("targetFile=", "")
                        
                        if build is None or targetfile is None:
                            print("Error: Config file is either corrupted or \"vandalized\"")
                            raise SystemExit(1)
                        else:
                            lastupdate = os.path.getmtime(targetfile)
                            try:
                                while True:
                                    time.sleep(1)
                                
                                    newupdate = os.path.getmtime(targetfile)
                                    if newupdate != lastupdate:
                                        lastupdate = newupdate
                                        build += 1
                                        path = "sodi/sodi_config.txt"
                                        with open(path, "r", encoding="utf-8") as f:
                                            content = f.read()

                                        content = content.replace(f"{build - 1}", f"{build}")

                                        with open(path, "w", encoding="utf-8") as f:
                                            f.write(content)
                                                
                                            
                            except KeyboardInterrupt as e:
                                print("Program stopped!")
                            except Exception as e:
                                print("Error: " + str(e))
        except FileNotFoundError:
            print("Error: Project doesn't exist.")
        except Exception as e:
            print("Error: " + str(e))
        
    else:
        print("Error: Invalid Arguments")
            
else:
    print("Sodi v1.0- commands:\nmake - make a sodi project\nrun - run a sodi project in this folder")