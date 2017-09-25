class Common:
  def __init__(self):
    self.base_url = 'http://localhost:8983/solr/'
    self.core = 'temp'

    self.response = 'response'
    self.docs = 'docs'
    self.no_docs = 'numFound'

    self.select = self.base_url + self.core + '/select'
    self.update = self.base_url + self.core + '/update'
    self.delete = self.base_url + self.core + '/update'

    self.headers = {
      "json":{"content-type" : "application/json" },
      "xml":{"content-type" : "text/xml" },
      "csv":{"content-type" : "text/csv" } 
    }