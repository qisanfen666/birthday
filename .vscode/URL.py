class url_manager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_url(self,url):
        if url is None or len(url)==0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_url(url)

    def get_url(self):
        if self.has_url():
            url=self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
        
    def has_url(self):
        return len(self.new_urls)>0

