class Page:
    def __init__(self, i: dict) -> None:
        self.header: dict = i['header']
        self.header_size = i['header']['size']
        self.body: dict = i['body']

    def render(self) -> dict:
        page_out = {'header': self.header['data'], 'body': self.body['data']}