class Robot:
    import unittest
    import random
    if not hasattr(unittest.TestCase, "assertRegex"):
        assertRegex = unittest.TestCase.assertRegexpMatches

    name_re = r'^[A-Z]{2}\d{3}$'

    def test_has_name(self):
        self.assertRegex(Robot().name, self.name_re)

    def test_name_sticks(self):
        robot = Robot()
        robot.name
        self.assertEqual(robot.name, robot.name)

    def test_different_robots_have_different_names(self):
        self.assertNotEqual(
            Robot().name,
            Robot().name
        )

    def test_reset_name(self):
        seed = "Totally random."

    random.seed(seed)
    robot = Robot()
    name = robot.name
    random.seed(seed)
    robot.reset()
    name2 = robot.name
    self.assertNotEqual(name, name2)
        self.assertRegex(name2, self.name_re)


if __name__ == '__main__':
    unittest.main()
