from ai_assistant.load import load_text


def test_load_text_returns_file_content(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello resume", encoding="utf-8")

    result = load_text(str(file))

    assert result == "hello resume"
