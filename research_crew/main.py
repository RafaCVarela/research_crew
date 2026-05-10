import os
from dotenv import load_dotenv
from research_crew.crew import ResearchCrew

# Crie o diretório de saída se não existir
os.makedirs('output', exist_ok=True)

def run():
    """
    Rodar a crew de pesquisa.
    """
    inputs = {
        'topic': """computação de borda de sistemas embarcados e IoT para ESP32 aplicados em
        computação em nuvem, nas seguintes plataformas, AWS, Google Cloud Plataform e Microsoft Azure"""
    }

    # Criar e rodar a crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Imprimir o resultado
    print("\n\n=== RELATÓRIO FINAL ===\n\n")
    print(result.raw)

    print("\n\nRelatório salvo em output/report.md")

if __name__ == "__main__":
    run()