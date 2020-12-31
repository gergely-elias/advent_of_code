import json
import requests
import os
import bs4
import readchar
import subprocess
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))

configfile = open(os.path.join(script_directory, "telescope_config.json"), "r")
config = json.loads(configfile.read())
configfile.close()

year, day, level = config["year"], config["day"], config["level"]

command = None
message = None
output = None
while command != "q":
    os.system("clear")
    print(year, "Day", day, "Level", level)
    print()
    print("[y] - change year")
    print("[d] - change day")
    print("[l] - change level")
    print("[i] - download input & initialize source")
    print("[r] - run")
    print("[s] - submit")
    print("[q] - quit")
    print()
    if message is not None:
        print(message)
        message = None
    print("> ", end="", flush=True)
    command = readchar.readkey()
    print(command)

    if command in "ydl":
        if command == "y":
            print("change year (2015..)")
            try:
                year = int(input("> "))
                if year < 2015:
                    year = 2015
                    message = "value out of bounds, using " + str(year) + " instead\n"
                year = str(year)
            except ValueError:
                message = "invalid value"
        elif command == "d":
            print("change year (1..25)")
            try:
                day = int(input("> "))
                if not 1 <= day <= 25:
                    day = min(25, max(1, day))
                    message = "value out of bounds, using " + str(day) + " instead\n"
                day = str(day)
            except ValueError:
                message = "invalid value"
        elif command == "l":
            print("change level (1/2)")
            try:
                level = int(input("> "))
                if not 1 <= level <= 2:
                    level = min(2, max(1, level))
                    message = "value out of bounds, using " + str(level) + " instead\n"
                level = str(level)
            except ValueError:
                message = "invalid value"
        config = {"year": year, "day": day, "level": level}
        configfile = open(os.path.join(script_directory, "telescope_config.json"), "w")
        configfile.write(json.dumps(config, indent=2))
        configfile.close()
    elif command == "i":
        cookiefile = open(os.path.join(script_directory, "cookie.json"), "r")
        cookies = json.loads(cookiefile.read())
        cookiefile.close()

        response = requests.get(
            "https://adventofcode.com/" + year + "/day/" + day + "/input",
            cookies=cookies,
        )
        message = "HTTP Response " + str(response.status_code) + "\n"
        if response.ok:
            message += "download successful\n"
        else:
            message += response.reason + "\n"
            exit()

        inputfile = open(
            os.path.join(script_directory, year, "inputd" + ("0" + day)[-2:] + ".txt"),
            "w",
        )
        inputfile.write(response.text)
        inputfile.close()

        sourcetemplate = "template.py"
        sourcefile = os.path.join(year, "d" + ("0" + day)[-2:] + "p" + level + ".py")
        if not os.path.exists(sourcefile):
            shutil.copyfile(sourcetemplate, sourcefile)
    elif command == "s":
        answer = input(
            "value to submit?"
            + (" (default: " + output + ")" if output is not None else "")
            + "\n> "
        )
        if answer == "" and output is not None:
            answer = output
        cookiefile = open(os.path.join(script_directory, "cookie.json"), "r")
        cookies = json.loads(cookiefile.read())
        cookiefile.close()

        response = requests.post(
            "https://adventofcode.com/" + year + "/day/" + day + "/answer",
            cookies=cookies,
            data={"level": level, "answer": answer},
        )
        message = "HTTP Response " + str(response.status_code) + "\n"
        if response.ok:
            response_html = response.text
            message += "\n"
        else:
            message += response.reason + "\n"
            exit()

        parsed_html = (
            bs4.BeautifulSoup(response_html, "html.parser")
            .find("article")
            .get_text()
            .replace("\r", "")
        )
        message += parsed_html + "\n\n"

        if not parsed_html.startswith("You gave an answer too recently;"):
            output = None
        if parsed_html.startswith("That's the right answer!"):
            level = str(int(level) + 1)
            if level == "3":
                level = "1"
                day = str(int(day) + 1)
            config = {"year": year, "day": day, "level": level}
            configfile = open(
                os.path.join(script_directory, "telescope_config.json"), "w"
            )
            configfile.write(json.dumps(config, indent=2))
            configfile.close()
            if day == "25" and level == "2":
                response = requests.post(
                    "https://adventofcode.com/" + year + "/day/" + day + "/answer",
                    cookies=cookies,
                    data={"level": level, "answer": "0"},
                )
                message += "HTTP Response " + str(response.status_code) + "\n"
                if response.ok:
                    response_html = response.text
                    message += "\n"
                    output = None
                else:
                    message += response.reason + "\n"
                    exit()

                parsed_html = (
                    bs4.BeautifulSoup(response_html, "html.parser")
                    .find("article")
                    .get_text()
                )
                message += parsed_html + "\n\n"

    elif command == "r":
        sourcefile = os.path.join(year, "d" + ("0" + day)[-2:] + "p" + level + ".py")
        inputfile = os.path.join(year, "inputd" + ("0" + day)[-2:] + ".txt")
        if os.path.exists(inputfile) and os.path.exists(sourcefile):
            try:
                output = (
                    subprocess.check_output(
                        "python3 " + sourcefile + " " + inputfile, shell=True
                    )
                    .decode("ascii")
                    .strip()
                )
                message = output + "\n"
            except subprocess.CalledProcessError:
                print("")
                print("press any key to go back to the menu", end="", flush=True)
                readchar.readkey()
        else:
            message = "input or source file not available\n"
    else:
        message = "invalid command\n"
