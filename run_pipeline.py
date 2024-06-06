from pipeline.dataclean import DataCleanPipeline
Clean = DataCleanPipeline()
Clean.RunSteps()
Clean.saveData()


from pipeline.datascaling import DataScalePipeline
Scale = DataScalePipeline()
Scale.RunPipeline()
Scale.savedata()

from pipeline.Modelpipeline import ModelBuildPipeline
Model = ModelBuildPipeline()
Model.RunSteps()
