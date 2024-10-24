

class SendBot:
    def __init__(self):
        with open("../../../PycharmProjects/Yui/Yui/links-manganelo.txt") as f:
            self.data = f.readlines()

    def create_profile(self):
        archive_list = []
        for link in self.data:
            archive = {
                "manga": link.split("|")[0],
                "chat_id": link.split("|")[1].strip("\n"),
            }
            archive_list.append(archive)
        return archive_list

