import argostranslate.package
import argostranslate.translate

from_code = "pb"
to_code = "es"

text_to_translate = """
Dicas para Melhorar seu Aprendizado

Estabeleça uma Rotina

Dedique pelo menos 30 minutos por dia aos seus estudos

Faça Anotações
Anote os pontos principais para fixar melhor o conteúdo
Pratique o que Aprendeu
Aplique os conhecimentos em projetos práticos.

...

Descubra milhares de cursos online ministrados por especialistas. Desenvolva suas habilidades no seu próprio ritmo.
"""

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

package_to_install = next(
    filter(
        # lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        lambda x: True, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate(text_to_translate, from_code, to_code)
print(translatedText)
