from pydub import AudioSegment

class CompatibilityChecker:
    def is_compatible(self, file, criteria):
        # Check if a file meets the compatibility criteria
        audio_file = AudioSegment.from_file(file)
        return (audio_file.frame_rate in criteria['sample_rates'] and
                audio_file.format in criteria['acceptable_formats'])
