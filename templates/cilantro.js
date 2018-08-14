var csrf_token = '{{ csrf_token }}',

    require = {
        baseUrl: '{{ STATIC_URL }}cilantro/js',
        paths: {
            'project': '{{ JAVASCRIPT_URL }}'
        }
    },

    cilantro = {
        url: '{% url "serrano:root" %}',
        root: '{{ request.META.SCRIPT_NAME }}',
        main: '#content',
        rootFieldId: 55,   // Used to provide a counts of subject while cilantro is loading
        rootLabel: 'subjects', // Used with subject_field_id 
        statsModelsList: [],
        threshold: 10000,
	fields: {
            defaults: {
                stats: false,
                form: {
                    controls: ['infoBars']
                }
            },
            instances: {
                // Sma type
                75: {
                    form: {
                        stats: false
                    }
                }
            }
	}

    };
