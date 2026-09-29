import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_animal(self):
        state = core.new_game()
        self.assertTrue(core.register(state, "A1"))
        self.assertFalse(core.register(state, "A1"))

    def test_02_enclosure_capacity(self):
        state = core.new_game()
        core.place(state, "A1", "E1")
        core.place(state, "A2", "E1")
        result = core.place(state, "A3", "E1")
        self.assertFalse(result)

    def test_03_feed_days_exact(self):
        state = core.new_game()
        self.assertEqual(core.feed_days(state, "A1", 4), 3)

    def test_04_cancel_feed_refunds(self):
        state = core.new_game()
        state["feed"] = 90
        core.cancel_feed(state, "A1", 10)
        self.assertEqual(state["feed"], 100)

    def test_05_no_treat_with_absent_vet(self):
        state = core.new_game()
        result = core.treat(state, "A1", "V2")
        self.assertFalse(result)

    def test_06_feed_failure_no_cost(self):
        state = core.new_game()
        state["feed"] = 5
        result = core.feed_animal(state, "A1", 10)
        self.assertFalse(result)
        self.assertEqual(state["feed"], 5)

    def test_07_disease_once(self):
        state = core.new_game()
        core.register(state, "A1")
        core.disease(state, "A1")
        self.assertEqual(state["animals"]["A1"]["health"], 90)

    def test_08_load_preserves_animal_id(self):
        state = core.new_game()
        state["animal_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["animal_id"], 4)


if __name__ == "__main__":
    unittest.main()
