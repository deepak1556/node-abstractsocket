{
  'targets': [
    {
      'target_name': 'bindings',
      'conditions': [
          ['OS=="linux"', {
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'defines': [ '_GNU_SOURCE=1' ],
            'sources': [ 'src/abstract_socket.cc' ],
          }],
      ],
      'include_dirs': [
        '<!(node -p "require(\'node-addon-api\').include_dir")',
      ]
    }
  ]
}
