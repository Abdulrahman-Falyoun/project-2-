class TenseModel:
    def __init__(self, tense_segments: list):
        self.segments = tense_segments
        self.tense = None
        if self.tense is None:
            self.find_tense(self.get_normal_pattern())

    @staticmethod
    def get_normal_pattern():
        return {
            'SimplePresent': [{'_': ['VBZ', 'VBP', 'VB']}],
            'SimplePresentModal_One': [{'have': ['VBZ', 'VBP']}],
            'SimplePresentModal_Two': [{'_all_modal_': ['MD']}, {'_': ['VB']}],
            'PresentContinuous': [{'be': ['VBZ', 'VBP']}, {'_': ['VBG']}],
            'SimplePast': [{'_': ['VBD']}],
            'PastContinuous': [{'be': ['VBD']}, {'_': ['VBG']}],
            'PresentPerfect': [{'have': ['VBZ', 'VBP']}, {'_': ['VBN']}],
            'PresentPerfectContinuous': [{'have': ['VBZ', 'VBP']}, {'be': ['VBN']}, {'_': ['VBG']}],
            'PastPerfect': [{'have': ['VBD']}, {'_': ['VBN']}],
            'PastPerfectContinuous': [{'have': ['VBD']}, {'be': ['VBN']}, {'_': ['VBG']}],
            'FuturePerfect': [{'will': ['MD']}, {'have': ['VB']}, {'_': ['VBN']}],
            'FuturePerfectContinuous': [{'will': ['MD']}, {'have': ['VB']}, {'be': ['VBN']}, {'_': ['VBG']}],
            'SimpleFuture': [{'will': ['MD']}, {'_': ['VB']}],
            'FutureContinuous': [{'will': ['MD']}, {'be': ['VB']}, {'_': ['VBG']}],
        }

    def find_tense(self, patterns):
        for tense_name, tense_pattern in patterns.items():
            if len(tense_pattern) != len(self.segments):
                continue

            for index, segment_pattern in enumerate(tense_pattern):
                if len(self.segments) > index and self.segments[index] is not None:
                    tense_segment = self.segments[index]
                    if '_' in segment_pattern and len(self.segments) == index + 1:
                        if tense_segment.tag in segment_pattern['_']:
                            self.tense = tense_name
                            return True
                    if tense_segment.lemma in segment_pattern:
                        if tense_segment.tag in segment_pattern[tense_segment.lemma]:
                            if tense_segment.lemma in segment_pattern:
                                continue

                    elif tense_segment.lemma in ['can', 'could', 'may', 'might', 'shall', 'should']:
                        if '_all_modal_' in segment_pattern:
                            continue
                    elif tense_segment.lemma == 'have' and len(self.segments) == 1:
                        self.tense = tense_name
                        return True
                    break
        return False
