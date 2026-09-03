import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "lessons" / "V2-LESSON-MAP.json"


class LessonV2MapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        cls.lessons = cls.data["lessons"]

    def test_legacy_front_matter_cannot_define_v2_readiness(self):
        self.assertFalse(
            self.data["rules"]["legacy_front_matter_may_define_v2_readiness"]
        )

    def test_m00_active_slice_contains_manual_execution_boundary(self):
        for lesson_id in ("6.1", "6.2", "6.3", "7.1"):
            self.assertEqual(self.lessons[lesson_id]["v2_mission_refs"], ["M00"])

    def test_history_lessons_map_to_m03(self):
        for lesson_id in ("3.1", "3.2", "3.3", "4.1", "4.2", "4.3"):
            self.assertEqual(self.lessons[lesson_id]["v2_mission_refs"], ["M03"])

    def test_grounded_ai_active_slice_is_chapter_8(self):
        for lesson_id in ("8.1", "8.2", "8.3"):
            self.assertEqual(self.lessons[lesson_id]["v2_mission_refs"], ["M04"])
            self.assertEqual(self.lessons[lesson_id]["body_generation"], "v2")
        for lesson_id in ("5.1", "5.2", "5.3"):
            self.assertEqual(self.lessons[lesson_id]["v2_role"], "reference")

    def test_v2_projection_has_no_hard_lesson_chain(self):
        for lesson_id, meta in self.lessons.items():
            self.assertEqual(meta["hard_prerequisites"], [], lesson_id)


if __name__ == "__main__":
    unittest.main()
