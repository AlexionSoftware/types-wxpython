from .generator import DocumentationGenerator

# Development: First setup to read everything once to a JSON file
# import generator.generator
# generator.generator.DEV_WRITE_TO_JSON_FILE = True
# generator.generator.DEV_READ_FROM_JSON_FILE = False

# Development: After first setup, read only from JSON file to speed up the process
# import generator.generator
# generator.generator.DEV_WRITE_TO_JSON_FILE = False
# generator.generator.DEV_READ_FROM_JSON_FILE = True

dg = DocumentationGenerator()
dg.generate()
