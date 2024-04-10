# Databricks notebook source
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

# COMMAND ----------

print(fibonacci(10))

# COMMAND ----------

# MAGIC %md
# MAGIC # Header 1
# MAGIC ## Header 2
# MAGIC **bold text**
# MAGIC *italics text*
# MAGIC ~~strikethrough text~~
# MAGIC `monospace text`
# MAGIC ---
# MAGIC > Block quote
# MAGIC Ordered list:
# MAGIC 1. Item 1
# MAGIC 1. Item 2
# MAGIC 1. Item 3
# MAGIC Unordered list:
# MAGIC - Item a
# MAGIC - Item b
# MAGIC - Item c
# MAGIC
