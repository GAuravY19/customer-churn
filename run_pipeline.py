from pipeline.dataclean import DataCleanPipeline

Clean = DataCleanPipeline()
Clean.RunSteps()
Clean.saveData()
