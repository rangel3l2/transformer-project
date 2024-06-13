
import numpy as np
import matplotlib.pyplot as plt

# Função para converter valores normalizados em coordenadas do triângulo
def to_triangle_coords(water, dielectric, neutralization, triangle_vertices):
    x = (1 - neutralization) * triangle_vertices[0][0] + dielectric * triangle_vertices[1][0] + neutralization * triangle_vertices[2][0]
    y = (1 - neutralization) * triangle_vertices[0][1] + dielectric * triangle_vertices[1][1] + neutralization * triangle_vertices[2][1]
    return x, y

# Função para gerar e plotar o triângulo de Durval com os pontos de análise
def generate_durval_triangle(analisys):
    # Definição dos vértices do triângulo de Durval
    triangle_vertices = np.array([
        [0, 0],   # Teor de água
        [1, 0],   # Fator de perdas dielétricas
        [0.5, np.sqrt(3)/2]  # Índice de neutralização
    ])

    # Configuração do gráfico
    plt.figure(figsize=(8, 8))
    plt.plot(triangle_vertices[:, 0], triangle_vertices[:, 1], 'k-', lw=2)
    plt.fill(triangle_vertices[:, 0], triangle_vertices[:, 1], 'lightgray', alpha=0.5)

    for item in analisys:
        # Normalização dos valores
        normalized_water_content = item['parameter']['water_content'] / 100.0
        normalized_dielectric_loss_factor = item['parameter']['dielectric_loss_factors90g']
        normalized_neutralized_number = item['parameter']['indice_neutralization']

        # Conversão para coordenadas do triângulo
        point_x, point_y = to_triangle_coords(
            normalized_water_content,
            normalized_dielectric_loss_factor,
            normalized_neutralized_number,
            triangle_vertices
        )

        # Plotando o ponto
        plt.plot(point_x, point_y, 'ro', markersize=10, label=f"Sample {item['id']}" if 'id' in item else 'Sample')

    # Anotação dos vértices
    plt.text(triangle_vertices[0][0], triangle_vertices[0][1] - 0.05, 'Teor de Água', ha='center')
    plt.text(triangle_vertices[1][0], triangle_vertices[1][1] - 0.05, 'Fator de Perdas Dieletricas', ha='center')
    plt.text(triangle_vertices[2][0], triangle_vertices[2][1] + 0.05, 'Índice de Neutralização', ha='center')

    # Formatação do gráfico
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, np.sqrt(3)/2 + 0.1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Durval Triangle')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

    
    # Salvar o gráfico em um arquivo
    plt.savefig('durval_triangle.png')
    plt.close()
    pass
# Exemplo de uso
# analisys = [
#     {
#         'id': 1,
#         'parameter': {
#             'teorAgua': 50.0,
#             'fatorPerdasDieletricas90g': 0.02,
#             'indiceNeutralizacao': 0.05
#         }
#     },
#     {
#         'id': 2,
#         'parameter': {
#             'teorAgua': 80.0,
#             'fatorPerdasDieletricas90g': 0.03,
#             'indiceNeutralizacao': 0.07
#         }
#     }
# ]

# generate_durval_triangle(analisys)


