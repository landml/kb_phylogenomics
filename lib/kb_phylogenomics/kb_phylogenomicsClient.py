# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_phylogenomics(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def view_tree(self, params, context=None):
        """
        :param params: instance of type "view_tree_Input" (view_tree() ** **
           show a KBase Tree and make newick and images downloadable) ->
           structure: parameter "workspace_name" of type "workspace_name" (**
           Common types), parameter "input_tree_ref" of type "data_obj_ref",
           parameter "desc" of String
        :returns: instance of type "view_tree_Output" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_tree',
                                        [params], self._service_ver, context)

    def run_DomainAnnotation_Sets(self, params, context=None):
        """
        :param params: instance of type "run_DomainAnnotation_Sets_Input"
           (run_DomainAnnotation_Sets() ** ** run the DomainAnnotation App
           against a GenomeSet) -> structure: parameter "workspace_name" of
           type "workspace_name" (** Common types), parameter
           "input_genomeSet_ref" of type "data_obj_ref", parameter
           "override_annot" of type "bool"
        :returns: instance of type "run_DomainAnnotation_Sets_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.run_DomainAnnotation_Sets',
                                        [params], self._service_ver, context)

    def view_fxn_profile(self, params, context=None):
        """
        :param params: instance of type "view_fxn_profile_Input"
           (view_fxn_profile() ** ** show a table/heatmap of general
           categories or custom gene families for a set of Genomes) ->
           structure: parameter "workspace_name" of type "workspace_name" (**
           Common types), parameter "input_genomeSet_ref" of type
           "data_obj_ref", parameter "namespace" of String, parameter
           "custom_target_fams" of type "CustomTargetFams" (parameter groups)
           -> structure: parameter "target_fams" of list of String, parameter
           "extra_target_fam_groups_COG" of list of String, parameter
           "extra_target_fam_groups_PFAM" of list of String, parameter
           "extra_target_fam_groups_TIGR" of list of String, parameter
           "extra_target_fam_groups_SEED" of list of String, parameter
           "count_category" of String, parameter "heatmap" of type "bool",
           parameter "vertical" of type "bool", parameter "top_hit" of type
           "bool", parameter "e_value" of Double, parameter "log_base" of
           Double, parameter "show_blanks" of type "bool"
        :returns: instance of type "view_fxn_profile_Output" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_fxn_profile',
                                        [params], self._service_ver, context)

    def view_fxn_profile_featureSet(self, params, context=None):
        """
        :param params: instance of type "view_fxn_profile_featureSet_Input"
           (view_fxn_profile_featureSet() ** ** show a table/heatmap of
           general categories or custom gene families for a set of Genomes)
           -> structure: parameter "workspace_name" of type "workspace_name"
           (** Common types), parameter "input_featureSet_ref" of type
           "data_obj_ref", parameter "namespace" of String, parameter
           "custom_target_fams" of type "CustomTargetFams" (parameter groups)
           -> structure: parameter "target_fams" of list of String, parameter
           "extra_target_fam_groups_COG" of list of String, parameter
           "extra_target_fam_groups_PFAM" of list of String, parameter
           "extra_target_fam_groups_TIGR" of list of String, parameter
           "extra_target_fam_groups_SEED" of list of String, parameter
           "count_category" of String, parameter "heatmap" of type "bool",
           parameter "vertical" of type "bool", parameter "top_hit" of type
           "bool", parameter "e_value" of Double, parameter "log_base" of
           Double, parameter "show_blanks" of type "bool"
        :returns: instance of type "view_fxn_profile_featureSet_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_fxn_profile_featureSet',
                                        [params], self._service_ver, context)

    def view_fxn_profile_phylo(self, params, context=None):
        """
        :param params: instance of type "view_fxn_profile_phylo_Input"
           (view_fxn_profile_phylo() ** ** show a table/heatmap of general
           categories or custom gene families for a set of Genomes using the
           species tree) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter
           "input_speciesTree_ref" of type "data_obj_ref", parameter
           "namespace" of String, parameter "custom_target_fams" of type
           "CustomTargetFams" (parameter groups) -> structure: parameter
           "target_fams" of list of String, parameter
           "extra_target_fam_groups_COG" of list of String, parameter
           "extra_target_fam_groups_PFAM" of list of String, parameter
           "extra_target_fam_groups_TIGR" of list of String, parameter
           "extra_target_fam_groups_SEED" of list of String, parameter
           "count_category" of String, parameter "heatmap" of type "bool",
           parameter "vertical" of type "bool", parameter "top_hit" of type
           "bool", parameter "e_value" of Double, parameter "log_base" of
           Double, parameter "show_blanks" of type "bool"
        :returns: instance of type "view_fxn_profile_phylo_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_fxn_profile_phylo',
                                        [params], self._service_ver, context)

    def view_genome_circle_plot(self, params, context=None):
        """
        :param params: instance of type "view_genome_circle_plot_Input"
           (view_genome_circle_plot() ** ** build a circle plot of a
           microbial genome) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter "input_genome_ref"
           of type "data_obj_ref"
        :returns: instance of type "view_genome_circle_plot_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_genome_circle_plot',
                                        [params], self._service_ver, context)

    def view_pan_circle_plot(self, params, context=None):
        """
        :param params: instance of type "view_pan_circle_plot_Input"
           (view_pan_circle_plot() ** ** build a circle plot of a microbial
           genome with its pangenome members) -> structure: parameter
           "workspace_name" of type "workspace_name" (** Common types),
           parameter "input_genome_ref" of type "data_obj_ref", parameter
           "input_pangenome_ref" of type "data_obj_ref", parameter
           "input_compare_genome_refs" of type "data_obj_ref", parameter
           "input_outgroup_genome_refs" of type "data_obj_ref", parameter
           "save_featuresets" of type "bool"
        :returns: instance of type "view_pan_circle_plot_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_pan_circle_plot',
                                        [params], self._service_ver, context)

    def view_pan_accumulation_plot(self, params, context=None):
        """
        :param params: instance of type "view_pan_accumulation_plot_Input"
           (view_pan_accumulation_plot() ** ** build an accumulation plot of
           a pangenome) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter "input_genome_ref"
           of type "data_obj_ref", parameter "input_pangenome_ref" of type
           "data_obj_ref"
        :returns: instance of type "view_pan_accumulation_plot_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_pan_accumulation_plot',
                                        [params], self._service_ver, context)

    def view_pan_flower_venn(self, params, context=None):
        """
        :param params: instance of type "view_pan_flower_venn_Input"
           (view_pan_flower_venn() ** ** build a multi-member pangenome
           flower venn diagram) -> structure: parameter "workspace_name" of
           type "workspace_name" (** Common types), parameter
           "input_genome_ref" of type "data_obj_ref", parameter
           "input_pangenome_ref" of type "data_obj_ref"
        :returns: instance of type "view_pan_flower_venn_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_pan_flower_venn',
                                        [params], self._service_ver, context)

    def view_pan_pairwise_overlap(self, params, context=None):
        """
        :param params: instance of type "view_pan_pairwise_overlap_Input"
           (view_pan_pairwise_overlap() ** ** build a multi-member pangenome
           pairwise overlap plot) -> structure: parameter "workspace_name" of
           type "workspace_name" (** Common types), parameter
           "input_genome_ref" of type "data_obj_ref", parameter
           "input_pangenome_ref" of type "data_obj_ref"
        :returns: instance of type "view_pan_pairwise_overlap_Output" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_pan_pairwise_overlap',
                                        [params], self._service_ver, context)

    def view_pan_phylo(self, params, context=None):
        """
        :param params: instance of type "view_pan_phylo_Input"
           (view_pan_phylo() ** ** show the pangenome accumulation using a
           tree) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter
           "input_pangenome_ref" of type "data_obj_ref", parameter
           "input_speciesTree_ref" of type "data_obj_ref", parameter
           "save_featuresets" of type "bool"
        :returns: instance of type "view_pan_phylo_Output" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.view_pan_phylo',
                                        [params], self._service_ver, context)

    def find_homologs_with_genome_context(self, params, context=None):
        """
        :param params: instance of type
           "find_homologs_with_genome_context_Input"
           (find_homologs_with_genome_context() ** ** show homolgous genes
           across multiple genomes within genome context against species
           tree) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter
           "input_featureSet_ref" of type "data_obj_ref", parameter
           "input_speciesTree_ref" of type "data_obj_ref", parameter
           "save_per_genome_featureSets" of type "bool", parameter
           "neighbor_thresh" of Long, parameter "ident_thresh" of Double,
           parameter "overlap_fraction" of Double, parameter "e_value" of
           Double, parameter "bitscore" of Double, parameter "color_seed" of
           Double
        :returns: instance of type "find_homologs_with_genome_context_Output"
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_phylogenomics.find_homologs_with_genome_context',
                                        [params], self._service_ver, context)

    def get_configure_categories(self, params, context=None):
        """
        :param params: instance of type "get_configure_categories_Input"
           (get_configure_categories() ** ** configure the domain categorie
           names and descriptions) -> structure: parameter "params" of type
           "view_fxn_profile_Input" (view_fxn_profile() ** ** show a
           table/heatmap of general categories or custom gene families for a
           set of Genomes) -> structure: parameter "workspace_name" of type
           "workspace_name" (** Common types), parameter
           "input_genomeSet_ref" of type "data_obj_ref", parameter
           "namespace" of String, parameter "custom_target_fams" of type
           "CustomTargetFams" (parameter groups) -> structure: parameter
           "target_fams" of list of String, parameter
           "extra_target_fam_groups_COG" of list of String, parameter
           "extra_target_fam_groups_PFAM" of list of String, parameter
           "extra_target_fam_groups_TIGR" of list of String, parameter
           "extra_target_fam_groups_SEED" of list of String, parameter
           "count_category" of String, parameter "heatmap" of type "bool",
           parameter "vertical" of type "bool", parameter "top_hit" of type
           "bool", parameter "e_value" of Double, parameter "log_base" of
           Double, parameter "show_blanks" of type "bool"
        :returns: instance of type "get_configure_categories_Output" ->
           structure: parameter "cats" of list of String, parameter
           "cat2name" of type "Cat2Name" (category to name) -> structure:
           parameter "namespace" of type "domain_source" (COG, PF, TIGR,
           SEED), parameter "cat" of type "category" (Categories), parameter
           "cat2group" of type "Cat2Group" (category to group) -> structure:
           parameter "namespace" of type "domain_source" (COG, PF, TIGR,
           SEED), parameter "cat" of type "category" (Categories), parameter
           "domfam2cat" of type "DomFam2Cat" (domain family to category) ->
           structure: parameter "namespace" of type "domain_source" (COG, PF,
           TIGR, SEED), parameter "domfam" of type "domainfamily" (Domains),
           parameter "cat2domfams" of type "Cat2DomFams" (category to domain
           family) -> structure: parameter "namespace" of type
           "domain_source" (COG, PF, TIGR, SEED), parameter "cat" of type
           "category" (Categories)
        """
        return self._client.call_method('kb_phylogenomics.get_configure_categories',
                                        [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_phylogenomics.status',
                                        [], self._service_ver, context)
