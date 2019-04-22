import unittest
from services.LinkerService import linkerService
from services.KgizeService import kgService
from settings import BASE_DIR
import os


class TestLinkIngService(unittest.TestCase):

    def test_parse(self):
        with open(os.path.join(BASE_DIR, "resources", "one_cv.json"), 'r', encoding='utf8') as f:
            self.json_str = f.read()
        self.cv = linkerService.parse(self.json_str)
        print(self.cv.__dict__)
        result_academy = linkerService.link_academy(self.cv)
        print(result_academy)
        result_company = linkerService.link_company(self.cv)
        print(result_company)
        result_linked = linkerService.link_terminology(self.cv)
        print(result_linked)
        result = kgService.kgsizer(self.cv, result_linked, result_academy, result_company)
        print(result)
        result = kgService.kgsizer_4tupe(self.cv, result_linked, result_academy, result_company)
        print(result)


if __name__ == '__main__':
    unittest.main()