from ai_assistant.screener import ResumeScreener
from ai_assistant.load import load_text
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Loading resume and job description...")
        resume = load_text("resume.txt")
        job = load_text("job.txt")
        screener = ResumeScreener()
        logger.info("Starting screening")    
        result = screener.screen(resume, job)
        print("Result: ", result)
        logger.info("Screening completed successfully.")
    except FileNotFoundError as e:
        logger.error("File problem: %s", e)
    except Exception as e:
        logger.error("Screening failed: %s: %s", type(e).__name__, e)
        logger.error("Details: %s", getattr(e, "body", None))


if __name__ == "__main__":
    main()
