import unittest
from BaciloKoch import load_functions, calc_functions

class TestBaciloKochFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Creating classes dataset")
        cls.classes_df = load_functions.read_classes("data/tb_functions.pl")
        cls.functions_df = load_functions.read_functions("data/tb_functions.pl")

    def test_df_columns(self):
        print("Testing dataframe number of columns")
        self.assertEqual(len(self.classes_df.columns), 6)
        self.assertEqual(len(self.functions_df.columns), 4)

    def test_read_orfs_info(self):
        print("Testing ORFs relationships")
        self.assertEqual(load_functions.read_orfs_info("data/orfs/tb_data_00.txt")['tb3071'],
                         ['tb1887', 'tb3131', 'tb2620', 'tb1760', 'tb2212', 'tb3721', 'tb1770'])

    def test_get_classes(self):
        print("Testing get_classes function")
        self.assertIn("1,0,0,0", calc_functions.get_classes())

    def test_get_classes_by_type(self):
        print("Testing get_classes_by_type function")
        self.assertEqual(calc_functions.get_classes_by_type("Degradation"), ["1,1,0,0"])
        self.assertEqual(calc_functions.get_classes_by_type("Respiration"), ["1,2,6,0"])


    def test_get_ORFs_in_class(self):
        print("Testing get_ORFs_in_class function")
        test_list = calc_functions.get_ORFs_in_class("1,1,1,0")
        self.assertIn('tb186', test_list)
        self.assertIn('tb727', test_list)
        self.assertNotIn('tb1905', test_list)


    def test_get_ORFs_by_pattern(self):
        print("Testing get_ORFs_by_pattern function")
        test_list = calc_functions.get_ORFs_by_pattern("protein")
        self.assertEqual(len(test_list), 294)


if __name__ == '__main__':
    unittest.main()
