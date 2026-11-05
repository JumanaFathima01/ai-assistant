from ai_assistant.screener import ResumeScreener
from ai_assistant.load import load_text


def main():
    try:
        resume = load_text("resume.txt")
        job = load_text("job.txt")
        screener = ResumeScreener()
        result = screener.screen(resume, job)
        print("Result: ", result)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("ERROR TYPE:", type(e).__name__)
        print("MESSAGE:", e)
        print("BODY:", getattr(e, "body", None))
        print("URL:", getattr(getattr(e, "request", None), "url", None))


if __name__ == "__main__":
    main()
