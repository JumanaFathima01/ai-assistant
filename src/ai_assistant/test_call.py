from ai_assistant.screener import ResumeScreener
from ai_assistant.load import load_text

screener = ResumeScreener()

result = screener.screen(load_text("resume.txt"), load_text("job.txt"))

print("Result: ", result)
