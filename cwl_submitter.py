import os
import io
import yaml
import pprint
import cwltool
import cwltool.factory
import os
import pprint


class CwlSubmitter:

    def __init__(self, cwl_path, cwl_inputs, files_list):
        self.cwl_path = cwl_path
        self.cwl_inputs = cwl_inputs
        self.files_list = files_list
        self.pp = pprint.PrettyPrinter(indent=4)

    def load_dedup_bams(self):
        with open(self.files_list) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        content = list(filter(lambda x: x.endswith('bam'), content))
        return content

    def load_cwl_inputs(self):
        with open(self.cwl_inputs, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return data

    def write_cwl_inputs(self, input_data):
        with io.open(self.cwl_inputs, 'w', encoding='utf8') as outfile:
            yaml.dump(input_data, outfile, default_flow_style=False, allow_unicode=True)

    def execute_cwl(self, inputs):
        runtime_context = cwltool.context.RuntimeContext()
        runtime_context.outdir = os.getcwd()
        fac = cwltool.factory.Factory(runtime_context=runtime_context)
        fac_obj = fac.make(self.cwl_path)
        # output_dir = os.path.dirname(os.path.realpath(__file__))
        self.pp.pprint(inputs)
        result = fac_obj(**inputs)
        self.pp.pprint(result)
        return 'Job Submitted'

    def loop_and_execute(self):
        input_data = self.load_cwl_inputs()
        bam_list = self.load_dedup_bams()
        for bam in bam_list:
            input_data['InputFile']['location'] = bam
            self.write_cwl_inputs(input_data)
            self.execute_cwl(input_data)
