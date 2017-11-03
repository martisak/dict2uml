from dict2uml import dict2plantuml


def test_answer():
    assert dict2plantuml({}) == \
        '@startuml\nclass "root" as root {\n\t.. Properties ..\n}\n\n@enduml'
