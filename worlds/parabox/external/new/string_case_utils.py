from dataclasses import dataclass
from enum import Enum


class CharCase(Enum):
    Lower = 0
    Upper = 1


@dataclass(frozen=True)
class WordCaseDefinition:
    first: CharCase
    other: CharCase


class WordCase:
    Lower = WordCaseDefinition(CharCase.Lower, CharCase.Lower)
    """lower"""
    Upper = WordCaseDefinition(CharCase.Upper, CharCase.Upper)
    """UPPER"""
    Title = WordCaseDefinition(CharCase.Upper, CharCase.Lower)
    """Title"""


@dataclass(frozen=True)
class NameCaseDefinition:
    first: WordCaseDefinition
    other: WordCaseDefinition
    seperator: str


class NameCase:
    Lower = NameCaseDefinition(WordCase.Lower, WordCase.Lower, "")
    """lowercase"""
    Upper = NameCaseDefinition(WordCase.Upper, WordCase.Upper, "")
    """UPPERCASE"""
    Title = NameCaseDefinition(WordCase.Title, WordCase.Lower, "")
    """Titlecase"""
    Camel = NameCaseDefinition(WordCase.Lower, WordCase.Title, "")
    """camelCase"""
    Pascal = NameCaseDefinition(WordCase.Title, WordCase.Title, "")
    """PascalCase"""
    Snake = NameCaseDefinition(WordCase.Lower, WordCase.Lower, "_")
    """snake_case"""
    Kebab = NameCaseDefinition(WordCase.Lower, WordCase.Lower, "-")
    """kebab-case"""
    Macro = NameCaseDefinition(WordCase.Upper, WordCase.Upper, "_")
    """MACRO_CASE"""
    Train = NameCaseDefinition(WordCase.Title, WordCase.Title, "-")
    """Train-Case"""
    WordTitle = NameCaseDefinition(WordCase.Title, WordCase.Title, " ")
    """Word Title Case"""
    WordLower = NameCaseDefinition(WordCase.Lower, WordCase.Lower, " ")
    """word lower case"""
    WordUpper = NameCaseDefinition(WordCase.Upper, WordCase.Upper, " ")
    """WORD UPPER CASE"""


def char_to_case(char: str, case: CharCase) -> str:
    match case:
        case CharCase.Lower:
            return char.lower()
        case CharCase.Upper:
            return char.upper()


def is_char_case(char: str, case: CharCase) -> bool:
    match case:
        case CharCase.Lower:
            return not char.isupper()
        case CharCase.Upper:
            return not char.islower()


def word_to_case(word: str, case: WordCaseDefinition) -> str:
    if not word:
        return ""
    return (
            char_to_case(word[0], case.first)
            + "".join([char_to_case(char, case.other) for char in word[1:]])
    )


def words_to_case(words: list[str], case: NameCaseDefinition) -> str:
    if not words:
        return ""
    items = (
            [word_to_case(words[0], case.first)]
            + [word_to_case(word, case.other) for word in words[1:]]
    )
    return case.seperator.join(items)


def _unseperated_to_words(name: str, case: NameCaseDefinition) -> list[str]:
    result = []
    word = []
    word_case = case.first
    name_iter = iter(name)
    first_char = next(name_iter)
    try:
        while True:
            word.append(first_char)
            while is_char_case(char := next(name_iter), word_case.other):
                word.append(char)
            else:
                first_char = char
            result.append("".join(word))
            word.clear()
            word_case = case.other
    except StopIteration:
        if word:
            result.append("".join(word))
        return result


def to_words(name: str, case: NameCaseDefinition) -> list[str]:
    if case.seperator:
        if case.seperator in name:
            return name.split(case.seperator)
        else:
            return [name]
    else:
        if case.other.first == case.other.other:
            return [name]
        return _unseperated_to_words(name, case)


def to_case(name: str, original: NameCaseDefinition, new: NameCaseDefinition):
    return words_to_case(to_words(name, original), new)


if __name__ == '__main__':
    print(words_to_case(["hey", "world"], NameCase.Macro))
    print(to_words("test Fish", NameCase.WordTitle))
    print(to_case("Possess", NameCase.Pascal, NameCase.Snake))
    print(to_case("test__test_f", NameCaseDefinition(WordCase.Lower, WordCase.Lower, "__"), NameCase.WordLower))
