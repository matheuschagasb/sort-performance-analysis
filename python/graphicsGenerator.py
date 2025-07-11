import matplotlib.pyplot as plt # type: ignore
import csv
import os
import sys

csv_path = 'resultados.csv'

if not os.path.exists(csv_path):
    print(f"\nArquivo '{csv_path}' não encontrado. Execute o programa C antes de rodar este script.\n")
    sys.exit(1)

tamanhos = []
tempos_selection_sort = []
tempos_insertion_sort = []
tempos_bubble_sort = []
tempos_merge_sort = []
tempos_quick_sort = []
tempos_heap_sort = []

with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tamanhos.append(int(row['Tamanho']))
        tempos_selection_sort.append(float(row['Selection']))
        tempos_insertion_sort.append(float(row['Insertion']))
        tempos_bubble_sort.append(float(row['Bubble']))
        tempos_merge_sort.append(float(row['Merge']))
        tempos_quick_sort.append(float(row['Quick']))
        tempos_heap_sort.append(float(row['Heap']))

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_selection_sort, label="Selection Sort")
plt.plot(tamanhos, tempos_insertion_sort, label="Insertion Sort")
plt.plot(tamanhos, tempos_bubble_sort, label="Bubble Sort")
plt.plot(tamanhos, tempos_merge_sort, label="Merge Sort")
plt.plot(tamanhos, tempos_quick_sort, label="Quick Sort")
plt.plot(tamanhos, tempos_heap_sort, label="Heap Sort")

plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo de execução (segundos)")
plt.title("Comparação de Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.yscale("log")

output_path = 'grafico_ordenacao.png'

try:
    plt.savefig(output_path)
    if os.path.exists(output_path):
        print(f"\nGráfico salvo com sucesso em '{output_path}'.\n")
    else:
        print(f"\nErro: o gráfico não foi salvo em '{output_path}'.\n")
except Exception as e:
    print(f"\nOcorreu um erro ao salvar o gráfico: {e}\n")
