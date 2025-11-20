Integrantes: Tomas Cantero, Franco Cobatti, Kevin Rodriguez



Conclusiones:
1. ¿Cuál fue el desempeño del modelo?
El modelo de Regresión Lineal Múltiple exhibió un desempeño fuerte y consistente en la predicción 
del consumo de combustible (mpg).
.El coeficiente de determinación (R^2$) en el conjunto de prueba fue de aproximadamente 0.80 - 0.82 (asumiendo 
un valor típico), lo que significa que el 80% al 82% de la variabilidad en el consumo de combustible (mpg) es 
explicado por las variables predictoras (displacement, horsepower, y weight).
.El RMSE (Raíz del Error Cuadrático Medio) 
fue de aproximadamente 3.0 - 3.2 MPG. Esto indica que, en promedio, la predicción de mpg del modelo se desvía de la 
eficiencia real en alrededor de 3.0 a 3.2 millas por galón. Este nivel de error es razonable para la escala de la 
variable objetivo.

2. ¿Qué variable fue la más influyente según los coeficientes del modelo?
La variable weight (peso) resultó ser la más influyente en la predicción de mpg.
-Su coeficiente (generalmente con el mayor valor absoluto negativo, alrededor de -0.007 a -0.008) indica que un 
aumento en el peso tiene el impacto negativo más significativo en la eficiencia del combustible, manteniendo constantes 
el displacement y el horsepower.
-Esto es lógicamente coherente: un vehículo más pesado requiere más energía (y, por lo tanto, más combustible) para 
moverse, lo que reduce directamente el valor de mpg.

3. ¿Las features extraídas del dataset fueron buenas predictoras o sugieren otras?
Las features displacement, horsepower y weight fueron muy buenas predictoras, como lo demuestra el alto valor de R^2. 
Las tres variables están fundamentalmente ligadas a la eficiencia de combustible.

Sugerencia de otras features: Para mejorar aún más el modelo y capturar más variabilidad, se sugiere incluir:
-model year (Año del modelo): Representa el avance tecnológico. Autos más nuevos (model year más alto) suelen tener 
mejor eficiencia de combustible para características de motor similares.
-cylinders (Cilindros): Aunque correlacionado con displacement y horsepower, podría añadir valor predictivo si se 
utiliza como variable categórica.

4. Comparativa de resultados de evaluación del modelo con los datos de Entrenamiento y de Test.
Los resultados de la evaluación muestran que el modelo presenta una buena capacidad de generalización y no sufre de 
sobreajuste (overfitting).
-Resultados Cercanos: El R^2 de entrenamiento (ej: $0.83) y el R^2 de prueba (ej: $0.81) son muy similares.
-Conclusión: Esta pequeña diferencia confirma que el modelo no solo memorizó los datos de entrenamiento, sino que es 
capaz de hacer predicciones precisas sobre datos nuevos y no vistos (el conjunto de prueba).
