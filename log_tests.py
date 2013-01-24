import unittest
class tests(unittest.TestCase):
    def setUp(self):
        @log
        def func(a,b):
            return(a-b)
        self.a=2
        self.b=1
        func(self.a,self.b)
    def test_read(self):
        self.assertTrue(open('log_file.txt','r'))
    def test_time(self):
        f=open('log_file.txt','r')
        lines=f.readlines()
        parts=(lines[-1]).split()
        string=parts[0]+" "+(parts[1])[:-7]
        self.assertEqual(str(datetime.now())[:-7], string)
    def test_name(self):
        f=open('log_file.txt','r')
        lines=f.readlines()
        parts=(lines[-1]).split()
        self.assertEqual('func',parts[2])
    def test_args(self):
        f=open('log_file.txt','r')
        lines=f.readlines()
        parts=(lines[-1]).split()
        self.assertEqual('(2, 1)',parts[3]+" "+parts[4])
