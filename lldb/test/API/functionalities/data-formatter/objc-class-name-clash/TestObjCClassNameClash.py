"""
Test that the ObjC "Class" synthetic provider does not
hide children of a C++ class named "Class".
"""

import lldb
from lldbsuite.test.lldbtest import *
import lldbsuite.test.lldbutil as lldbutil


class ObjCClassNameClashTestCase(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.line = line_number("main.cpp", "// break here")

    def test_cpp_class_named_Class_shows_children(self):
        """A C++ class named 'Class' should not be hijacked by the ObjC formatter."""
        self.build()

        _, _, _, _ = lldbutil.run_to_line_breakpoint(
            self, lldb.SBFileSpec("main.cpp"), self.line
        )

        self.expect("frame variable sample1", substrs=["x = 1"])

        self.expect(
            "frame variable sample", matching=False, substrs=["x = 1"]
        )
