import config as Config

class Parser:

    debug: bool = False
    verbose: bool = False
    test_connectivity: bool = False
    show_examples: bool = False
    api_authentication_method: str = ""
    api_key_file_path: str = ""
    database_filename: str = ""
    enable_logging: bool = False
    log_filename: str = ""
    log_max_bytes_per_file: int = 0
    log_max_number_log_files: int = 0
    log_level: int = 0
    log_format: str = ""
    use_proxy: bool = False
    proxy_url: str = ""
    proxy_port: int = 0
    proxy_username: str = ""
    proxy_password: str = ""
    verify_https_certificate = True

    # static methods
    @staticmethod
    def parse_configuration(p_args, p_config: Config) -> None:
        Parser.verbose = p_args.verbose
        Parser.version = p_args.version
        Parser.debug = (p_args.debug if p_args.debug else p_config.DEBUG)
        Parser.api_authentication_method = p_config.API_AUTHENTICATION_METHOD
        Parser.api_credential_format = p_config.API_CREDENTIAL_FORMAT
        Parser.api_key_file_path = p_config.API_KEY_FILE_PATH
        Parser.api_connection_timeout = p_config.API_CONNECTION_TIMEOUT
        Parser.verify_https_certificate = p_config.VERIFY_HTTPS_CERTIFICATE
        Parser.database_filename = p_config.DATABASE_FILENAME
        Parser.enable_logging = p_config.LOG_ENABLE_LOGGING
        Parser.log_filename = p_config.LOG_FILENAME
        Parser.log_max_bytes_per_file = p_config.LOG_MAX_BYTES_PER_FILE
        Parser.log_max_number_log_files = p_config.LOG_MAX_NUMBER_LOG_FILES
        Parser.log_level = p_config.LOG_LEVEL
        Parser.log_format = p_config.LOG_FORMAT
        Parser.use_proxy = p_config.USE_PROXY
        Parser.proxy_url = p_config.PROXY_URL
        Parser.proxy_port = p_config.PROXY_PORT
        Parser.proxy_username = p_config.PROXY_USERNAME
        Parser.proxy_password = p_config.PROXY_PASSWORD

        Parser.show_examples = p_args.examples
        Parser.show_usage = p_args.usage
        Parser.test_connectivity = p_args.test

        # Universal options
        Parser.page_number = p_args.page_number
        Parser.page_size = p_args.page_size
        Parser.input_filename = p_args.input_filename

        # Account
        Parser.get_account = p_args.get_account
        Parser.get_license = p_args.get_license

        # Agents
        Parser.get_agents = p_args.get_agents

        # Discovered Services
        Parser.get_discovered_services = p_args.get_discovered_services
        Parser.download_discovered_services = p_args.download_discovered_services
        Parser.output_filename = p_args.output_filename
        Parser.output_separator = p_args.output_separator

        # Scans
        Parser.get_scans = p_args.get_scans
        Parser.get_scans_by_website = p_args.get_scans_by_website
        Parser.website_url = p_args.website_url
        Parser.target_url = p_args.target_url
        Parser.initiated_date_sort_direction = p_args.initiated_date_sort_direction

        # Scan Profiles
        Parser.get_scan_profiles = p_args.get_scan_profiles
        Parser.get_scan_profile = p_args.get_scan_profile
        Parser.scan_profile_id = p_args.scan_profile_id
        Parser.scan_profile_name = p_args.scan_profile_name

        # Team Member
        Parser.get_team_member = p_args.get_team_member
        Parser.team_member_id = p_args.team_member_id
        Parser.team_member_email = p_args.team_member_email

        # Team Members
        Parser.get_team_members = p_args.get_team_members
        Parser.get_account_managers = p_args.get_account_managers
        Parser.get_website_managers = p_args.get_website_managers
        Parser.get_api_accounts = p_args.get_api_accounts
        Parser.get_scan_accounts = p_args.get_scan_accounts
        Parser.get_disabled_accounts = p_args.get_disabled_accounts

        # Technologies
        Parser.get_technologies = p_args.get_technologies
        Parser.get_obsolete_technologies = p_args.get_obsolete_technologies
        Parser.technology_name = p_args.technology_name

        # Website
        Parser.get_website_by_url = p_args.get_website_by_url
        Parser.get_website_by_name = p_args.get_website_by_name
        Parser.get_website_by_id = p_args.get_website_by_id

        Parser.website_url = p_args.website_url
        Parser.website_name = p_args.website_name
        Parser.website_id = p_args.website_id

        if Parser.get_website_by_url:
            Parser.query = Parser.website_url
        if Parser.get_website_by_name:
            Parser.query = Parser.website_name

        # Websites
        Parser.get_websites = p_args.get_websites
        Parser.upload_websites = p_args.upload_websites
        Parser.get_websites_by_group_name = p_args.get_websites_by_group_name
        Parser.get_websites_by_group_id = p_args.get_websites_by_group_id

        Parser.website_group_name = p_args.website_group_name
        Parser.website_group_id = p_args.website_group_id

        if Parser.get_websites_by_group_name:
            Parser.query = Parser.website_group_name
        if Parser.get_websites_by_group_id:
            Parser.query = Parser.website_group_id

        # Website Groups
        Parser.get_website_groups = p_args.get_website_groups
        Parser.upload_website_groups = p_args.upload_website_groups

        # Vulnerabilities
        Parser.get_vulnerability_templates = p_args.get_vulnerability_templates
        Parser.get_vulnerability_template = p_args.get_vulnerability_template
        Parser.get_vulnerability_types = p_args.get_vulnerability_types

        # Vulnerabilities Options
        Parser.report_policy_id = p_args.report_policy_id or ""
        Parser.vulnerability_type = p_args.vulnerability_type

        Parser.output_format = p_args.output_format.value.upper() if hasattr(p_args.output_format, 'value') else None

        # Auxiliary Features
        Parser.ping_sites = p_args.ping_sites
        Parser.ping_sites_in_file = p_args.ping_sites_in_file

        # Authetication Sites and Pages
        Parser.authentication_sites = p_config.AUTHENTICATION_SITES
        Parser.authentication_page_keywords = p_config.AUTHENTICATION_PAGE_KEYWORDS

        #Reporting Options
        Parser.unattended = p_args.unattended
        Parser.report_agents_missing_heartbeat = p_args.report_agents_missing_heartbeat
        Parser.agent_heartbeat_too_long_seconds = p_config.AGENT_HEARTBEAT_TOO_LONG_SECONDS
        Parser.agent_heartbeat_breadcrumb_filename = p_config.AGENT_HEARTBEAT_BREADCRUMB_FILENAME
        Parser.agent_heartbeat_notification_interval_minutes = p_config.AGENT_HEARTBEAT_NOTIFICATION_INTERVAL_MINUTES

        Parser.report_disabled_agents = p_args.report_disabled_agents
        Parser.disabled_agents_too_long_seconds = p_config.DISABLED_AGENTS_TOO_LONG_SECONDS
        Parser.disabled_agents_breadcrumb_filename = p_config.DISABLED_AGENTS_BREADCRUMB_FILENAME
        Parser.disabled_agents_notification_interval_minutes = p_config.DISABLED_AGENTS_NOTIFICATION_INTERVAL_MINUTES

        #Report Issues
        Parser.report_issues = p_args.report_issues
        Parser.report_summary = p_args.report_summary

        # Business Scorecard
        #Parser.report_business_scorecard = p_args.report_business_scorecard
