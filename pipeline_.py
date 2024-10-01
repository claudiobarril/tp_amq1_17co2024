from util import *

# Definir pipelines para preprocesamiento
preprocess_pipeline = Pipeline(steps=[
    ('split_name', SplitName()),
    ('impute_mileage', ImputeMileageWithCar()),
    ('Engine_maxpower',EnginePowerTransformer()),
    ('convert_mileage', ConvertMileageToKmpl()),
    ('impute_max_power', ImputeMaxPowerWithCar()),
    ('standardize_torque', StandardizeTorque()),
])

categorical_cols = ['fuel', 'seller_type', 'transmission', 'make']
columns_to_drop_for_imputation = []

full_pipeline = Pipeline(steps=[
    ('map_owner', MapOwner()),
    ('one_hot_encode', OneHotEncodeCategoricals(categorical_cols=categorical_cols)),
    ('iterative_imputation', IterativeImputation(columns_to_drop=columns_to_drop_for_imputation)),
    ('round_seats', RoundSeats()),
    ('scaler', StandardScaler())  # Agregar el StandardScaler aquí
])

# Pipeline final con preprocesamiento de datos y feature engineering
final_pipeline = Pipeline(steps=[
    ('preprocess', preprocess_pipeline),
    ('features', full_pipeline)
    
])

# Cargar y dividir los datos
data = pd.read_csv('Car details v3.csv')
X = data.drop('selling_price', axis=1)
y = data['selling_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Ajustar y transformar los datos
X_train_processed = final_pipeline.fit_transform(X_train)

# Recuperar las columnas finales
final_columns = final_pipeline.named_steps['features'].named_steps['round_seats'].final_columns_

# Convertir a DataFrame
X_train_processed_df = pd.DataFrame(X_train_processed, columns=final_columns)

# Mostrar las primeras filas
print("Training data processed head:")
print(X_train_processed_df.head(5))

X_test_processed = final_pipeline.transform(X_test)

# Usamos las mismas columnas finales que ya guardamos al transformar X_train
final_columns = final_pipeline.named_steps['features'].named_steps['round_seats'].final_columns_

# Convertir X_test_processed a un DataFrame, con las mismas columnas
X_test_processed_df = pd.DataFrame(X_test_processed, columns=final_columns)

# Mostrar las primeras filas de X_test
print("Test data processed head:")
print(X_test_processed_df.head(5))

output_dir = 'dataset_processed'
os.makedirs(output_dir, exist_ok=True)

# Guardar los DataFrames como archivos CSV
X_train_processed_df.to_csv(os.path.join(output_dir, 'X_train_processed.csv'), index=False)
X_test_processed_df.to_csv(os.path.join(output_dir, 'X_test_processed.csv'), index=False)

print("Archivos CSV guardados en el directorio 'dataset_processed'.")