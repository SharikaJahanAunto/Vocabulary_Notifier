from plyer import notification
if __name__ == "__main__":
    title = "Learn this vocab"
    with open("Vocabulary.txt") as vc:
        lines = vc.readlines()
        for vocab in lines:
            notification.notify(title = title, message= vocab.strip(), timeout= 10)